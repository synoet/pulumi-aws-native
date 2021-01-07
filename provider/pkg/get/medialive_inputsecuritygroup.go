package get

import (
	"context"

	"github.com/aws/aws-sdk-go/service/medialive"
)

func (g *Getter) getMediaLiveInputSecurityGroupAttributes(ctx context.Context, physicalResourceID string) (map[string]interface{}, error) {
	resp, err := g.medialive.DescribeInputSecurityGroupWithContext(ctx, &medialive.DescribeInputSecurityGroupInput{
		// Add params here
	})
	_ = resp
	if err != nil {
		return nil, err
	}

	attrs := map[string]interface{}{
		"Arn": nil,
	}
	return attrs, nil
}