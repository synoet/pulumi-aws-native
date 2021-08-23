// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html
 */
export class LocalGatewayRoute extends pulumi.CustomResource {
    /**
     * Get an existing LocalGatewayRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LocalGatewayRoute {
        return new LocalGatewayRoute(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:LocalGatewayRoute';

    /**
     * Returns true if the given object is an instance of LocalGatewayRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LocalGatewayRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LocalGatewayRoute.__pulumiType;
    }

    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-destinationcidrblock
     */
    public readonly destinationCidrBlock!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-localgatewayroutetableid
     */
    public readonly localGatewayRouteTableId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-localgatewayvirtualinterfacegroupid
     */
    public readonly localGatewayVirtualInterfaceGroupId!: pulumi.Output<string>;
    public /*out*/ readonly state!: pulumi.Output<string>;
    public /*out*/ readonly type!: pulumi.Output<string>;

    /**
     * Create a LocalGatewayRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LocalGatewayRouteArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.destinationCidrBlock === undefined) && !opts.urn) {
                throw new Error("Missing required property 'destinationCidrBlock'");
            }
            if ((!args || args.localGatewayRouteTableId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'localGatewayRouteTableId'");
            }
            if ((!args || args.localGatewayVirtualInterfaceGroupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'localGatewayVirtualInterfaceGroupId'");
            }
            inputs["destinationCidrBlock"] = args ? args.destinationCidrBlock : undefined;
            inputs["localGatewayRouteTableId"] = args ? args.localGatewayRouteTableId : undefined;
            inputs["localGatewayVirtualInterfaceGroupId"] = args ? args.localGatewayVirtualInterfaceGroupId : undefined;
            inputs["state"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        } else {
            inputs["destinationCidrBlock"] = undefined /*out*/;
            inputs["localGatewayRouteTableId"] = undefined /*out*/;
            inputs["localGatewayVirtualInterfaceGroupId"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(LocalGatewayRoute.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a LocalGatewayRoute resource.
 */
export interface LocalGatewayRouteArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-destinationcidrblock
     */
    destinationCidrBlock: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-localgatewayroutetableid
     */
    localGatewayRouteTableId: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-localgatewayvirtualinterfacegroupid
     */
    localGatewayVirtualInterfaceGroupId: pulumi.Input<string>;
}
