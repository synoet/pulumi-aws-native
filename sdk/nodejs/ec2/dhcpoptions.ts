// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::DHCPOptions
 */
export class DHCPOptions extends pulumi.CustomResource {
    /**
     * Get an existing DHCPOptions resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DHCPOptions {
        return new DHCPOptions(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:DHCPOptions';

    /**
     * Returns true if the given object is an instance of DHCPOptions.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DHCPOptions {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DHCPOptions.__pulumiType;
    }

    public /*out*/ readonly dhcpOptionsId!: pulumi.Output<string>;
    /**
     * This value is used to complete unqualified DNS hostnames.
     */
    public readonly domainName!: pulumi.Output<string | undefined>;
    /**
     * The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.
     */
    public readonly domainNameServers!: pulumi.Output<string[] | undefined>;
    /**
     * The IPv4 addresses of up to four NetBIOS name servers.
     */
    public readonly netbiosNameServers!: pulumi.Output<string[] | undefined>;
    /**
     * The NetBIOS node type (1, 2, 4, or 8).
     */
    public readonly netbiosNodeType!: pulumi.Output<number | undefined>;
    /**
     * The IPv4 addresses of up to four Network Time Protocol (NTP) servers.
     */
    public readonly ntpServers!: pulumi.Output<string[] | undefined>;
    /**
     * Any tags assigned to the DHCP options set.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.DHCPOptionsTag[] | undefined>;

    /**
     * Create a DHCPOptions resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DHCPOptionsArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["domainNameServers"] = args ? args.domainNameServers : undefined;
            resourceInputs["netbiosNameServers"] = args ? args.netbiosNameServers : undefined;
            resourceInputs["netbiosNodeType"] = args ? args.netbiosNodeType : undefined;
            resourceInputs["ntpServers"] = args ? args.ntpServers : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["dhcpOptionsId"] = undefined /*out*/;
        } else {
            resourceInputs["dhcpOptionsId"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["domainNameServers"] = undefined /*out*/;
            resourceInputs["netbiosNameServers"] = undefined /*out*/;
            resourceInputs["netbiosNodeType"] = undefined /*out*/;
            resourceInputs["ntpServers"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DHCPOptions.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DHCPOptions resource.
 */
export interface DHCPOptionsArgs {
    /**
     * This value is used to complete unqualified DNS hostnames.
     */
    domainName?: pulumi.Input<string>;
    /**
     * The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.
     */
    domainNameServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The IPv4 addresses of up to four NetBIOS name servers.
     */
    netbiosNameServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The NetBIOS node type (1, 2, 4, or 8).
     */
    netbiosNodeType?: pulumi.Input<number>;
    /**
     * The IPv4 addresses of up to four Network Time Protocol (NTP) servers.
     */
    ntpServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Any tags assigned to the DHCP options set.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.DHCPOptionsTagArgs>[]>;
}
