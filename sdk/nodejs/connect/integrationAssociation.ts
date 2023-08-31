// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::IntegrationAssociation
 */
export class IntegrationAssociation extends pulumi.CustomResource {
    /**
     * Get an existing IntegrationAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): IntegrationAssociation {
        return new IntegrationAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:connect:IntegrationAssociation';

    /**
     * Returns true if the given object is an instance of IntegrationAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IntegrationAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IntegrationAssociation.__pulumiType;
    }

    public readonly instanceId!: pulumi.Output<string>;
    public readonly integrationArn!: pulumi.Output<string>;
    public /*out*/ readonly integrationAssociationId!: pulumi.Output<string>;
    public readonly integrationType!: pulumi.Output<enums.connect.IntegrationAssociationIntegrationType>;

    /**
     * Create a IntegrationAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IntegrationAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            if ((!args || args.integrationArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'integrationArn'");
            }
            if ((!args || args.integrationType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'integrationType'");
            }
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["integrationArn"] = args ? args.integrationArn : undefined;
            resourceInputs["integrationType"] = args ? args.integrationType : undefined;
            resourceInputs["integrationAssociationId"] = undefined /*out*/;
        } else {
            resourceInputs["instanceId"] = undefined /*out*/;
            resourceInputs["integrationArn"] = undefined /*out*/;
            resourceInputs["integrationAssociationId"] = undefined /*out*/;
            resourceInputs["integrationType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["instanceId", "integrationArn", "integrationType"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(IntegrationAssociation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a IntegrationAssociation resource.
 */
export interface IntegrationAssociationArgs {
    instanceId: pulumi.Input<string>;
    integrationArn: pulumi.Input<string>;
    integrationType: pulumi.Input<enums.connect.IntegrationAssociationIntegrationType>;
}
