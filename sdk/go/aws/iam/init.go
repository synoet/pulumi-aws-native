// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "aws-native:iam:AccessKey":
		r = &AccessKey{}
	case "aws-native:iam:Group":
		r = &Group{}
	case "aws-native:iam:GroupPolicy":
		r = &GroupPolicy{}
	case "aws-native:iam:InstanceProfile":
		r = &InstanceProfile{}
	case "aws-native:iam:ManagedPolicy":
		r = &ManagedPolicy{}
	case "aws-native:iam:OidcProvider":
		r = &OidcProvider{}
	case "aws-native:iam:Policy":
		r = &Policy{}
	case "aws-native:iam:Role":
		r = &Role{}
	case "aws-native:iam:RolePolicy":
		r = &RolePolicy{}
	case "aws-native:iam:SamlProvider":
		r = &SamlProvider{}
	case "aws-native:iam:ServerCertificate":
		r = &ServerCertificate{}
	case "aws-native:iam:ServiceLinkedRole":
		r = &ServiceLinkedRole{}
	case "aws-native:iam:User":
		r = &User{}
	case "aws-native:iam:UserPolicy":
		r = &UserPolicy{}
	case "aws-native:iam:UserToGroupAddition":
		r = &UserToGroupAddition{}
	case "aws-native:iam:VirtualMfaDevice":
		r = &VirtualMfaDevice{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"aws-native",
		"iam",
		&module{version},
	)
}
