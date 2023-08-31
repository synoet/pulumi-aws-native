// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGateway::BasePathMapping
 */
export class BasePathMapping extends pulumi.CustomResource {
    /**
     * Get an existing BasePathMapping resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): BasePathMapping {
        return new BasePathMapping(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:BasePathMapping';

    /**
     * Returns true if the given object is an instance of BasePathMapping.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BasePathMapping {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BasePathMapping.__pulumiType;
    }

    /**
     * The base path name that callers of the API must provide in the URL after the domain name.
     */
    public readonly basePath!: pulumi.Output<string | undefined>;
    /**
     * The DomainName of an AWS::ApiGateway::DomainName resource.
     */
    public readonly domainName!: pulumi.Output<string>;
    /**
     * The ID of the API.
     */
    public readonly restApiId!: pulumi.Output<string | undefined>;
    /**
     * The name of the API's stage.
     */
    public readonly stage!: pulumi.Output<string | undefined>;

    /**
     * Create a BasePathMapping resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BasePathMappingArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.domainName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainName'");
            }
            resourceInputs["basePath"] = args ? args.basePath : undefined;
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["restApiId"] = args ? args.restApiId : undefined;
            resourceInputs["stage"] = args ? args.stage : undefined;
        } else {
            resourceInputs["basePath"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["restApiId"] = undefined /*out*/;
            resourceInputs["stage"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["basePath", "domainName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(BasePathMapping.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a BasePathMapping resource.
 */
export interface BasePathMappingArgs {
    /**
     * The base path name that callers of the API must provide in the URL after the domain name.
     */
    basePath?: pulumi.Input<string>;
    /**
     * The DomainName of an AWS::ApiGateway::DomainName resource.
     */
    domainName: pulumi.Input<string>;
    /**
     * The ID of the API.
     */
    restApiId?: pulumi.Input<string>;
    /**
     * The name of the API's stage.
     */
    stage?: pulumi.Input<string>;
}
