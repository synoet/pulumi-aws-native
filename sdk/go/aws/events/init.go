// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package events

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
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
	case "aws-native:events:ApiDestination":
		r = &ApiDestination{}
	case "aws-native:events:Archive":
		r = &Archive{}
	case "aws-native:events:Connection":
		r = &Connection{}
	case "aws-native:events:Endpoint":
		r = &Endpoint{}
	case "aws-native:events:EventBus":
		r = &EventBus{}
	case "aws-native:events:EventBusPolicy":
		r = &EventBusPolicy{}
	case "aws-native:events:Rule":
		r = &Rule{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := aws.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"aws-native",
		"events",
		&module{version},
	)
}
