// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html
 */
export class TransitGatewayPeeringAttachment extends pulumi.CustomResource {
    /**
     * Get an existing TransitGatewayPeeringAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TransitGatewayPeeringAttachment {
        return new TransitGatewayPeeringAttachment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:TransitGatewayPeeringAttachment';

    /**
     * Returns true if the given object is an instance of TransitGatewayPeeringAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TransitGatewayPeeringAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TransitGatewayPeeringAttachment.__pulumiType;
    }

    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peeraccountid
     */
    public readonly peerAccountId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peerregion
     */
    public readonly peerRegion!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peertransitgatewayid
     */
    public readonly peerTransitGatewayId!: pulumi.Output<string>;
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-tags
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public /*out*/ readonly transitGatewayAttachmentId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-transitgatewayid
     */
    public readonly transitGatewayId!: pulumi.Output<string>;

    /**
     * Create a TransitGatewayPeeringAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TransitGatewayPeeringAttachmentArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.peerAccountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerAccountId'");
            }
            if ((!args || args.peerRegion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerRegion'");
            }
            if ((!args || args.peerTransitGatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerTransitGatewayId'");
            }
            if ((!args || args.transitGatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'transitGatewayId'");
            }
            inputs["peerAccountId"] = args ? args.peerAccountId : undefined;
            inputs["peerRegion"] = args ? args.peerRegion : undefined;
            inputs["peerTransitGatewayId"] = args ? args.peerTransitGatewayId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["transitGatewayId"] = args ? args.transitGatewayId : undefined;
            inputs["creationTime"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["transitGatewayAttachmentId"] = undefined /*out*/;
        } else {
            inputs["creationTime"] = undefined /*out*/;
            inputs["peerAccountId"] = undefined /*out*/;
            inputs["peerRegion"] = undefined /*out*/;
            inputs["peerTransitGatewayId"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["transitGatewayAttachmentId"] = undefined /*out*/;
            inputs["transitGatewayId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(TransitGatewayPeeringAttachment.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a TransitGatewayPeeringAttachment resource.
 */
export interface TransitGatewayPeeringAttachmentArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peeraccountid
     */
    peerAccountId: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peerregion
     */
    peerRegion: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peertransitgatewayid
     */
    peerTransitGatewayId: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-tags
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-transitgatewayid
     */
    transitGatewayId: pulumi.Input<string>;
}
