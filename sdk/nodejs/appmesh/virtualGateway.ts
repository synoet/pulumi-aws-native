// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppMesh::VirtualGateway
 *
 * @deprecated VirtualGateway is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VirtualGateway extends pulumi.CustomResource {
    /**
     * Get an existing VirtualGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VirtualGateway {
        pulumi.log.warn("VirtualGateway is deprecated: VirtualGateway is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VirtualGateway(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appmesh:VirtualGateway';

    /**
     * Returns true if the given object is an instance of VirtualGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VirtualGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VirtualGateway.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly meshName!: pulumi.Output<string>;
    public readonly meshOwner!: pulumi.Output<string | undefined>;
    public /*out*/ readonly resourceOwner!: pulumi.Output<string>;
    public readonly spec!: pulumi.Output<outputs.appmesh.VirtualGatewaySpec>;
    public readonly tags!: pulumi.Output<outputs.appmesh.VirtualGatewayTag[] | undefined>;
    public /*out*/ readonly uid!: pulumi.Output<string>;
    public readonly virtualGatewayName!: pulumi.Output<string | undefined>;

    /**
     * Create a VirtualGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VirtualGateway is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VirtualGatewayArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VirtualGateway is deprecated: VirtualGateway is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.meshName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'meshName'");
            }
            if ((!args || args.spec === undefined) && !opts.urn) {
                throw new Error("Missing required property 'spec'");
            }
            resourceInputs["meshName"] = args ? args.meshName : undefined;
            resourceInputs["meshOwner"] = args ? args.meshOwner : undefined;
            resourceInputs["spec"] = args ? args.spec : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["virtualGatewayName"] = args ? args.virtualGatewayName : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["resourceOwner"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["meshName"] = undefined /*out*/;
            resourceInputs["meshOwner"] = undefined /*out*/;
            resourceInputs["resourceOwner"] = undefined /*out*/;
            resourceInputs["spec"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["virtualGatewayName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["meshName", "meshOwner", "virtualGatewayName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(VirtualGateway.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VirtualGateway resource.
 */
export interface VirtualGatewayArgs {
    meshName: pulumi.Input<string>;
    meshOwner?: pulumi.Input<string>;
    spec: pulumi.Input<inputs.appmesh.VirtualGatewaySpecArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.appmesh.VirtualGatewayTagArgs>[]>;
    virtualGatewayName?: pulumi.Input<string>;
}
