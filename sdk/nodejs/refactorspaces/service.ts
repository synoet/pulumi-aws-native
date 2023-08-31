// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::RefactorSpaces::Service Resource Type
 */
export class Service extends pulumi.CustomResource {
    /**
     * Get an existing Service resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Service {
        return new Service(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:refactorspaces:Service';

    /**
     * Returns true if the given object is an instance of Service.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Service {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Service.__pulumiType;
    }

    public readonly applicationIdentifier!: pulumi.Output<string>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly endpointType!: pulumi.Output<enums.refactorspaces.ServiceEndpointType>;
    public readonly environmentIdentifier!: pulumi.Output<string>;
    public readonly lambdaEndpoint!: pulumi.Output<outputs.refactorspaces.ServiceLambdaEndpointInput | undefined>;
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly serviceIdentifier!: pulumi.Output<string>;
    /**
     * Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
     */
    public readonly tags!: pulumi.Output<outputs.refactorspaces.ServiceTag[] | undefined>;
    public readonly urlEndpoint!: pulumi.Output<outputs.refactorspaces.ServiceUrlEndpointInput | undefined>;
    public readonly vpcId!: pulumi.Output<string | undefined>;

    /**
     * Create a Service resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.applicationIdentifier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationIdentifier'");
            }
            if ((!args || args.endpointType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpointType'");
            }
            if ((!args || args.environmentIdentifier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'environmentIdentifier'");
            }
            resourceInputs["applicationIdentifier"] = args ? args.applicationIdentifier : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["endpointType"] = args ? args.endpointType : undefined;
            resourceInputs["environmentIdentifier"] = args ? args.environmentIdentifier : undefined;
            resourceInputs["lambdaEndpoint"] = args ? args.lambdaEndpoint : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["urlEndpoint"] = args ? args.urlEndpoint : undefined;
            resourceInputs["vpcId"] = args ? args.vpcId : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["serviceIdentifier"] = undefined /*out*/;
        } else {
            resourceInputs["applicationIdentifier"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["endpointType"] = undefined /*out*/;
            resourceInputs["environmentIdentifier"] = undefined /*out*/;
            resourceInputs["lambdaEndpoint"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["serviceIdentifier"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["urlEndpoint"] = undefined /*out*/;
            resourceInputs["vpcId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["applicationIdentifier", "description", "endpointType", "environmentIdentifier", "lambdaEndpoint", "name", "urlEndpoint", "vpcId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Service.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Service resource.
 */
export interface ServiceArgs {
    applicationIdentifier: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    endpointType: pulumi.Input<enums.refactorspaces.ServiceEndpointType>;
    environmentIdentifier: pulumi.Input<string>;
    lambdaEndpoint?: pulumi.Input<inputs.refactorspaces.ServiceLambdaEndpointInputArgs>;
    name?: pulumi.Input<string>;
    /**
     * Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.refactorspaces.ServiceTagArgs>[]>;
    urlEndpoint?: pulumi.Input<inputs.refactorspaces.ServiceUrlEndpointInputArgs>;
    vpcId?: pulumi.Input<string>;
}
