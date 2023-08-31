// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::TransitGatewayRouteTablePropagation
 *
 * @deprecated TransitGatewayRouteTablePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class TransitGatewayRouteTablePropagation extends pulumi.CustomResource {
    /**
     * Get an existing TransitGatewayRouteTablePropagation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TransitGatewayRouteTablePropagation {
        pulumi.log.warn("TransitGatewayRouteTablePropagation is deprecated: TransitGatewayRouteTablePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new TransitGatewayRouteTablePropagation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:TransitGatewayRouteTablePropagation';

    /**
     * Returns true if the given object is an instance of TransitGatewayRouteTablePropagation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TransitGatewayRouteTablePropagation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TransitGatewayRouteTablePropagation.__pulumiType;
    }

    public readonly transitGatewayAttachmentId!: pulumi.Output<string>;
    public readonly transitGatewayRouteTableId!: pulumi.Output<string>;

    /**
     * Create a TransitGatewayRouteTablePropagation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated TransitGatewayRouteTablePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: TransitGatewayRouteTablePropagationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("TransitGatewayRouteTablePropagation is deprecated: TransitGatewayRouteTablePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.transitGatewayAttachmentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'transitGatewayAttachmentId'");
            }
            if ((!args || args.transitGatewayRouteTableId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'transitGatewayRouteTableId'");
            }
            resourceInputs["transitGatewayAttachmentId"] = args ? args.transitGatewayAttachmentId : undefined;
            resourceInputs["transitGatewayRouteTableId"] = args ? args.transitGatewayRouteTableId : undefined;
        } else {
            resourceInputs["transitGatewayAttachmentId"] = undefined /*out*/;
            resourceInputs["transitGatewayRouteTableId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["transitGatewayAttachmentId", "transitGatewayRouteTableId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(TransitGatewayRouteTablePropagation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a TransitGatewayRouteTablePropagation resource.
 */
export interface TransitGatewayRouteTablePropagationArgs {
    transitGatewayAttachmentId: pulumi.Input<string>;
    transitGatewayRouteTableId: pulumi.Input<string>;
}
