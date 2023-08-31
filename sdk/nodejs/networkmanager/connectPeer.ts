// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS::NetworkManager::ConnectPeer Resource Type Definition.
 */
export class ConnectPeer extends pulumi.CustomResource {
    /**
     * Get an existing ConnectPeer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConnectPeer {
        return new ConnectPeer(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:networkmanager:ConnectPeer';

    /**
     * Returns true if the given object is an instance of ConnectPeer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConnectPeer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConnectPeer.__pulumiType;
    }

    /**
     * Bgp options for connect peer.
     */
    public readonly bgpOptions!: pulumi.Output<outputs.networkmanager.ConnectPeerBgpOptions | undefined>;
    /**
     * Configuration of the connect peer.
     */
    public /*out*/ readonly configuration!: pulumi.Output<outputs.networkmanager.ConnectPeerConfiguration>;
    /**
     * The ID of the attachment to connect.
     */
    public readonly connectAttachmentId!: pulumi.Output<string>;
    /**
     * The ID of the Connect peer.
     */
    public /*out*/ readonly connectPeerId!: pulumi.Output<string>;
    /**
     * The IP address of a core network.
     */
    public readonly coreNetworkAddress!: pulumi.Output<string | undefined>;
    /**
     * The ID of the core network.
     */
    public /*out*/ readonly coreNetworkId!: pulumi.Output<string>;
    /**
     * Connect peer creation time.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The Connect peer Regions where edges are located.
     */
    public /*out*/ readonly edgeLocation!: pulumi.Output<string>;
    /**
     * The inside IP addresses used for a Connect peer configuration.
     */
    public readonly insideCidrBlocks!: pulumi.Output<string[] | undefined>;
    /**
     * The IP address of the Connect peer.
     */
    public readonly peerAddress!: pulumi.Output<string>;
    /**
     * State of the connect peer.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.networkmanager.ConnectPeerTag[] | undefined>;

    /**
     * Create a ConnectPeer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConnectPeerArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.connectAttachmentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connectAttachmentId'");
            }
            if ((!args || args.peerAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerAddress'");
            }
            resourceInputs["bgpOptions"] = args ? args.bgpOptions : undefined;
            resourceInputs["connectAttachmentId"] = args ? args.connectAttachmentId : undefined;
            resourceInputs["coreNetworkAddress"] = args ? args.coreNetworkAddress : undefined;
            resourceInputs["insideCidrBlocks"] = args ? args.insideCidrBlocks : undefined;
            resourceInputs["peerAddress"] = args ? args.peerAddress : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["configuration"] = undefined /*out*/;
            resourceInputs["connectPeerId"] = undefined /*out*/;
            resourceInputs["coreNetworkId"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["edgeLocation"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
        } else {
            resourceInputs["bgpOptions"] = undefined /*out*/;
            resourceInputs["configuration"] = undefined /*out*/;
            resourceInputs["connectAttachmentId"] = undefined /*out*/;
            resourceInputs["connectPeerId"] = undefined /*out*/;
            resourceInputs["coreNetworkAddress"] = undefined /*out*/;
            resourceInputs["coreNetworkId"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["edgeLocation"] = undefined /*out*/;
            resourceInputs["insideCidrBlocks"] = undefined /*out*/;
            resourceInputs["peerAddress"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["bgpOptions", "connectAttachmentId", "coreNetworkAddress", "insideCidrBlocks[*]", "peerAddress"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConnectPeer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConnectPeer resource.
 */
export interface ConnectPeerArgs {
    /**
     * Bgp options for connect peer.
     */
    bgpOptions?: pulumi.Input<inputs.networkmanager.ConnectPeerBgpOptionsArgs>;
    /**
     * The ID of the attachment to connect.
     */
    connectAttachmentId: pulumi.Input<string>;
    /**
     * The IP address of a core network.
     */
    coreNetworkAddress?: pulumi.Input<string>;
    /**
     * The inside IP addresses used for a Connect peer configuration.
     */
    insideCidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The IP address of the Connect peer.
     */
    peerAddress: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.networkmanager.ConnectPeerTagArgs>[]>;
}
