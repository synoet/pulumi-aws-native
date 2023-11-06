// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.
 */
export class ApiKey extends pulumi.CustomResource {
    /**
     * Get an existing ApiKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ApiKey {
        return new ApiKey(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:ApiKey';

    /**
     * Returns true if the given object is an instance of ApiKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiKey.__pulumiType;
    }

    public /*out*/ readonly apiKeyId!: pulumi.Output<string>;
    /**
     * An MKT customer identifier, when integrating with the AWS SaaS Marketplace.
     */
    public readonly customerId!: pulumi.Output<string | undefined>;
    /**
     * The description of the ApiKey.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Specifies whether the ApiKey can be used by callers.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies whether (``true``) or not (``false``) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.
     */
    public readonly generateDistinctId!: pulumi.Output<boolean | undefined>;
    /**
     * A name for the API key. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the API key name. For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
     *  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
     */
    public readonly stageKeys!: pulumi.Output<outputs.apigateway.ApiKeyStageKey[] | undefined>;
    /**
     * The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.
     */
    public readonly tags!: pulumi.Output<outputs.apigateway.ApiKeyTag[] | undefined>;
    /**
     * Specifies a value of the API key.
     */
    public readonly value!: pulumi.Output<string | undefined>;

    /**
     * Create a ApiKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApiKeyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["customerId"] = args ? args.customerId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["generateDistinctId"] = args ? args.generateDistinctId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["stageKeys"] = args ? args.stageKeys : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["value"] = args ? args.value : undefined;
            resourceInputs["apiKeyId"] = undefined /*out*/;
        } else {
            resourceInputs["apiKeyId"] = undefined /*out*/;
            resourceInputs["customerId"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["enabled"] = undefined /*out*/;
            resourceInputs["generateDistinctId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["stageKeys"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["value"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["generateDistinctId", "name", "value"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ApiKey.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ApiKey resource.
 */
export interface ApiKeyArgs {
    /**
     * An MKT customer identifier, when integrating with the AWS SaaS Marketplace.
     */
    customerId?: pulumi.Input<string>;
    /**
     * The description of the ApiKey.
     */
    description?: pulumi.Input<string>;
    /**
     * Specifies whether the ApiKey can be used by callers.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * Specifies whether (``true``) or not (``false``) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.
     */
    generateDistinctId?: pulumi.Input<boolean>;
    /**
     * A name for the API key. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the API key name. For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
     *  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
     */
    name?: pulumi.Input<string>;
    /**
     * DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
     */
    stageKeys?: pulumi.Input<pulumi.Input<inputs.apigateway.ApiKeyStageKeyArgs>[]>;
    /**
     * The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.apigateway.ApiKeyTagArgs>[]>;
    /**
     * Specifies a value of the API key.
     */
    value?: pulumi.Input<string>;
}
